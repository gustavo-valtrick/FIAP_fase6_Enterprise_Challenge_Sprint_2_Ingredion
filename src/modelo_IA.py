import importlib
import subprocess
import sys

# Função para instalar e importar pacotes
# 'os' é módulo padrão e não precisa ser instalado
def install_and_import(package, import_name=None):
    if import_name is None:
        import_name = package
    try:
        importlib.import_module(import_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[import_name] = importlib.import_module(import_name)

# Lista dos pacotes necessários com seus nomes para importação
required_packages = {
    "pandas": "pandas",
    "numpy": "numpy",
    "scikit-learn": "sklearn"
}

for package, import_name in required_packages.items():
    install_and_import(package, import_name)

# Agora, pode importar os módulos/submódulos normalmente
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def load_processed_data(processed_dir, raw_dir):
    ndvi = pd.read_csv(os.path.join(processed_dir, 'ndvi_clean.csv'), parse_dates=['date'])
    decomp = pd.read_csv(os.path.join(processed_dir, 'decomposition.csv'), parse_dates=['date'])
    prod = pd.read_csv(os.path.join(raw_dir, 'productivity_history.csv'), parse_dates=['date'])
    return ndvi, decomp, prod

def build_and_evaluate_model(ndvi, decomp, prod):
    # Merge dos DataFrames
    df = ndvi.merge(decomp, on='date').merge(prod, on='date')

    features = ['ndvi', 'trend', 'seasonal', 'resid']
    target = 'productivity'

    n_amostras = len(df)
    print(f'Total de amostras: {n_amostras}')

    if n_amostras < 4:
        print("ERRO: O dataset é muito pequeno para treino, teste e validação cruzada. Adicione mais dados.")
        return

    # Separar treino e teste
    test_size = max(0.5, 2 / n_amostras) if n_amostras > 2 else 0.5
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, shuffle=False
    )

    print(f"Amostras treino: {len(X_train)} | Amostras teste: {len(X_test)}")

    # Treinar modelo
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prever e avaliar
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print('RMSE:', rmse)
    if len(y_test) >= 2:
        print('R2:', r2_score(y_test, y_pred))
    else:
        print('R2: Não definido (menos de 2 amostras no teste)')

    # Ajuste de hiperparâmetros
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, 20, None]
    }
    cv_splits = min(3, len(X_train))
    if cv_splits < 2:
        print("Não há amostras suficientes para validação cruzada (GridSearchCV). Adicione mais dados.")
    else:
        grid = GridSearchCV(
            RandomForestRegressor(random_state=42),
            param_grid,
            cv=cv_splits,
            scoring='neg_mean_squared_error'
        )
        grid.fit(X_train, y_train)
        print('Melhores parâmetros:', grid.best_params_)

        # Avaliar o melhor modelo
        best_model = grid.best_estimator_
        y_pred_best = best_model.predict(X_test)
        rmse_best = np.sqrt(mean_squared_error(y_test, y_pred_best))
        print('Melhor RMSE:', rmse_best)
        if len(y_test) >= 2:
            print('Melhor R2:', r2_score(y_test, y_pred_best))
        else:
            print('Melhor R2: Não definido (menos de 2 amostras no teste)')

if __name__ == '__main__':
    # Ajuste os diretórios conforme sua estrutura
    processed_dir = r'E:\Sprint_2\data\processed'
    raw_dir = r'E:\Sprint_2\data\raw'
    ndvi, decomp, prod = load_processed_data(processed_dir, raw_dir)
    build_and_evaluate_model(ndvi, decomp, prod)


