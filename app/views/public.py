
from flask import render_template, Blueprint

public = Blueprint('public', __name__)


@public.route('/')
def index():
    """Serve home page."""
    return render_template('public/index.j2')

@public.route('/examples/one')
def example_one():
    """Serve example one page."""
    return render_template('public/examples/one.j2')

@public.route('/examples/two')
def example_two():
    """Serve example two page."""
    return render_template('public/examples/two.j2')