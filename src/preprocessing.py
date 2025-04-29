import importlib
import subprocess
import sys

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

# Lista dos pacotes necessários (nome do pacote no PyPI)
required_packages = {
    "pandas": "pandas",
    "statsmodels": "statsmodels"
}

for module_name, package_name in required_packages.items():
    install_and_import(package_name)

import os
import argparse
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def load_data(input_dir):
    """Carrega arquivos CSV brutos"""
    ndvi = pd.read_csv(os.path.join(input_dir, 'ndvi_timeseries.csv'), parse_dates=['date'])
    flags = pd.read_csv(os.path.join(input_dir, 'quality_flags.csv'), parse_dates=['date'])
    prod = pd.read_csv(os.path.join(input_dir, 'productivity_history.csv'), parse_dates=['date'])
    return ndvi, flags, prod


def clean_ndvi(ndvi, flags, quality_threshold=0.8):
    """
    Filtra por qualidade e interpola valores faltantes.
    Assume que flags contém coluna 'quality' de 0 a 1.
    """
    # Merge NDVI e qualidade
    df = ndvi.merge(flags, on=['date', 'pixel_id'], how='left')
    # Filtrar apenas registros com qualidade >= threshold
    df = df[df['quality'] >= quality_threshold]
    # Média espacial (todos pixels) por data
    daily = df.groupby('date')['ndvi'].mean().reset_index()
    # Preencher datas faltantes
    daily = daily.set_index('date').asfreq('D')
    # Interpolação linear
    daily['ndvi'] = daily['ndvi'].interpolate(method='time')
    daily = daily.reset_index()
    return daily


def decompose_series(daily, model='additive', period=46):
    """Aplica decomposição sazonal e retorna DataFrame com trend, seasonal e residuo."""
    series = daily.set_index('date')['ndvi']
    decomp = seasonal_decompose(series, model=model, period=period)
    result = pd.DataFrame({
        'date': series.index,
        'observed': decomp.observed,
        'trend': decomp.trend,
        'seasonal': decomp.seasonal,
        'resid': decomp.resid
    }).reset_index(drop=True)
    return result


def save_outputs(daily, decomposition, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    daily.to_csv(os.path.join(output_dir, 'ndvi_clean.csv'), index=False)
    decomposition.to_csv(os.path.join(output_dir, 'decomposition.csv'), index=False)


def main():
    parser = argparse.ArgumentParser(description='Pré-processamento NDVI')
    parser.add_argument('--input_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    args = parser.parse_args()

    ndvi, flags, prod = load_data(args.input_dir)
    daily = clean_ndvi(ndvi, flags)
    decomposition = decompose_series(daily)
    save_outputs(daily, decomposition, args.output_dir)
    print('Pré-processamento concluído. Arquivos salvos em', args.output_dir)

if __name__ == '__main__':
    main()


