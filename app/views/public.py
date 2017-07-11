
import os.path as op

import pandas as pd

from flask import render_template, Blueprint, current_app

public = Blueprint('public', __name__)


@public.route('/')
def index():
    """Serve home page."""
    return render_template('public/index.j2')

@public.route('/examples/one')
def example_one():
    """Serve example one page."""
    gps_data_path = op.join(current_app.config['STATIC_DIR'], 'data/gv01.csv')

    # read csv file to pandas dataframe (normally you'd use a database)
    data = pd.read_csv(gps_data_path, index_col=False)

    # some data aren't worth showing
    unwanted_columns = ['eUnc', 'nUnc', 'zUnc', 'eCov', 'nCov', 'zCov']

    # remove unwanted data columns in-place
    data.drop(unwanted_columns, axis=1, inplace=True)

    # spit out html table from dataframe
    table = data.to_html()

    return render_template('public/examples/one.j2', table=table)

@public.route('/examples/two')
def example_two():
    """Serve example two page."""
    return render_template('public/examples/two.j2')
