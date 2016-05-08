from vj4 import app
from vj4 import error
from vj4.view import base

@app.route('/lang/{lang}', 'language_set')
class LanguageView(base.View):
  @base.route_argument
  async def get(self, *, lang):
    if not lang in ['zh_CN', 'en']:
      raise error.ValidationError('lang')
    await self.set_settings(view_lang=lang)
    self.json_or_redirect(self.referer_or_main)
