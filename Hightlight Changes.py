import sublime, sublime_plugin
import types

class ClearChangesCommand(sublime_plugin.EventListener):
	def on_post_save(self, view):
		view.erase_regions('unsaved')

class HighlightUnsavedCommand(sublime_plugin.EventListener):
	def on_modified(self, view):
		
		unsaved = view.get_regions('unsaved') + [view.line(s) for s in view.sel()]

		if not isinstance(view.file_name(), type(None)):
			
			with open(view.file_name(), 'r') as f:
					read_data = str(f.read())

			for sel in view.sel():
				if read_data[view.line(sel).begin():view.line(sel).end()] == view.substr(view.line(sel)):
					unsaved[:] = [x for x in unsaved if x != view.line(sel)]

			view.add_regions("unsaved", unsaved, "mark", "dot", sublime.HIDDEN | sublime.PERSISTENT)
