import argparse
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import mlflow
import mlflow.sklearn
from rappiml.skutils.transformers import DateTimeTransformer
from rappiml.skutils.transformers import DropColumnsTransformer


def run(source, target):
    print("\nLoading data ...")
    orders_df = pd.read_csv(source)

    print("\nPreparing data for training ...")
    X = orders_df.drop(['taken'], axis=1)
    y = orders_df['taken']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42, stratify=y)

    scaling_features = [
        'to_user_distance', 'to_user_elevation', 'total_earning'
    ]
    datetime_features = ['created_at']

    print("\nTraining ...")
    preprocessor = ColumnTransformer(
        transformers=[
            ('datetime', DateTimeTransformer(onehot=True), datetime_features),
            ('continuous', StandardScaler(), scaling_features)
        ],
    )

    parameters = {
        'classifier__n_estimators': [100]
    }

    pipeline = Pipeline(
        steps=[
            (
                'dropcols',
                DropColumnsTransformer(cols=['store_id', 'order_id'])
            ),
            ('preprocessing', preprocessor),
            ('classifier', RandomForestClassifier())
        ]
    )

    clf = GridSearchCV(pipeline, parameters, scoring='roc_auc')
    clf.fit(X_train, y_train)

    best_model = clf.best_estimator_
    cv_score = clf.best_score_
    test_score = clf.score(X_test, y_test)

    print("CV score:", cv_score)
    print("Test score", test_score)
    print(best_model)

    print("\nSaving best model ...")

    mlflow.sklearn.save_model(
        best_model,
        path=target,
        serialization_format=mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE
    )

    print("Done.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train default model')

    parser.add_argument(
        '--input_csv',
        action="store",
        required=True,
        # default="data/orders.csv",
        help='Data source',
        dest="input_csv"
    )

    parser.add_argument(
        '--output_dir',
        action="store",
        required=True,
        help='Target directory',
        dest="output_dir"
    )

    # Parse arguments and print them
    args = parser.parse_args()
    print("Source file:", args.input_csv)
    print("Target dir:", args.output_dir)

    # Run
    run(args.input_csv, args.output_dir)
