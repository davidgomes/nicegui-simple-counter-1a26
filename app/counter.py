from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value in user storage
        if 'count' not in app.storage.user:
            app.storage.user['count'] = 0
        
        def increment():
            """Increment the counter and update display"""
            app.storage.user['count'] += 1
            counter_label.text = str(app.storage.user['count'])
        
        # Main container with minimal, clean background
        with ui.column().classes('items-center justify-center min-h-screen gap-20 bg-slate-50'):
            
            # Counter display - extremely large, clean digital typography
            counter_label = ui.label(str(app.storage.user['count'])).classes(
                'text-[16rem] font-thin text-slate-700 select-none tracking-wider '
                'drop-shadow-sm transition-all duration-200'
            ).mark('counter-display')
            
            # Circular increment button - unobtrusive and elegant
            ui.button('', icon='add').classes(
                'w-16 h-16 rounded-full bg-white hover:bg-slate-100 '
                'text-slate-500 hover:text-slate-600 shadow-lg hover:shadow-xl '
                'border-0 transition-all duration-300 ease-out '
                'focus:ring-2 focus:ring-slate-200 focus:ring-opacity-50 focus:outline-none '
                'active:scale-95 hover:scale-105'
            ).on_click(increment).mark('increment-button')