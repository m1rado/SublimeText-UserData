import sublime, sublime_plugin
class AutoCloseTagCommand(sublime_plugin.TextCommand):
    def run(self, edit, prefix=""):
        self.view.run_command('insert', {'characters': prefix})
        cursorPosition = self.view.sel()[0].begin() 
        self.view.run_command('close_tag')
        self.view.sel().clear()
        self.view.sel().add(cursorPosition)