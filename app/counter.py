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
        
        # Main container with centered layout and pristine background
        with ui.column().classes('items-center justify-center min-h-screen gap-16 bg-gray-50'):
            
            # Counter display - ultra-large, minimal typography
            counter_label = ui.label(str(app.storage.user['count'])).classes(
                'text-[12rem] font-extralight text-gray-800 select-none tracking-tight'
            ).mark('counter-display')
            
            # Increment button - refined, subtle design
            ui.button('', icon='add').classes(
                'w-14 h-14 rounded-full bg-white hover:bg-gray-50 '
                'text-gray-600 shadow-md hover:shadow-lg '
                'border border-gray-100 transition-all duration-300 '
                'focus:ring-1 focus:ring-gray-200 focus:outline-none'
            ).on_click(increment).mark('increment-button')