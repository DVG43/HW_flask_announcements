
from views import AnnounView
from errors import app

announ_view = AnnounView.as_view('announsments')
app.add_url_rule('/announsments/', view_func=announ_view, methods=['POST'])
app.add_url_rule('/announsments/<int:announsment_id>', view_func=announ_view, methods=['GET', 'DELETE'])

app.run()