
import config

from app import create_app

app = create_app(config, debug=True)
app.run()
