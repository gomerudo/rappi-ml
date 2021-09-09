# import os
import argparse
import logging
import sys
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
from rappiml.transformers import DateTimeTransformer
from rappiml.transformers import DropColumnsTransformer


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('RAPPI')


def run(source, target):
    logger.info("Loading data ...")
    orders_df = pd.read_csv(source)

    logger.info("Preparing data for training ...")
    X = orders_df.drop(['taken'], axis=1)
    y = orders_df['taken']
    X['created_at'] = X['created_at'].astype('datetime64[ns, UTC]')
    logger.info(X.dtypes)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42, stratify=y)

    scaling_features = [
        'to_user_distance', 'to_user_elevation', 'total_earning'
    ]
    datetime_features = 'created_at'

    logger.info("Training ...")
    preprocessor = ColumnTransformer(
        transformers=[
            ('datetime', DateTimeTransformer(onehot=True), datetime_features),
            ('continuous', StandardScaler(), scaling_features)
        ],
    )

    pipeline = Pipeline(
        steps=[
            (
                'dropcols',
                DropColumnsTransformer(cols=['store_id', 'order_id'])
            ),
            ('preprocessing', preprocessor),
            ('classifier', RandomForestClassifier(n_estimators=100))
        ]
    )

    pipeline.fit(X_train, y_train)

    test_score = pipeline.score(X_test, y_test)

    logger.info("Test score: %f" % test_score)

    logger.info("Obtaining input and ouput signature ...")

    signature = infer_signature(X_test, pipeline.predict(X_test))
    logger.info(signature)

    logger.info("Saving best model ...")

    mlflow.sklearn.save_model(
        pipeline,
        path=target,
        serialization_format=mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE,
        signature=signature,
        pip_requirements="/home/rappiml/requirements.txt"
    )

    logger.info("Done.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train default model')

    parser.add_argument(
        '--input_csv',
        action="store",
        required=True,
        help='Data source',
        dest="input_csv"
    )

    parser.add_argument(
        '--output_dir',
        action="store",
        required=True,
        help='Output directory',
        dest="output_dir"
    )

    # Parse arguments and print them
    args = parser.parse_args()

    # Run
    run(args.input_csv, args.output_dir)
