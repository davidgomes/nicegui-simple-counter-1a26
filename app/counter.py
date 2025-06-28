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
        
        # Main container with centered layout and clean background
        with ui.column().classes('items-center justify-center min-h-screen gap-12 bg-white'):
            
            # Counter display - large, clean typography
            counter_label = ui.label(str(app.storage.user['count'])).classes(
                'text-9xl font-thin text-gray-900 select-none'
            ).mark('counter-display')
            
            # Increment button - minimal, circular design
            ui.button('', icon='add').classes(
                'w-16 h-16 rounded-full bg-gray-100 hover:bg-gray-200 '
                'text-gray-700 shadow-sm transition-colors duration-200 '
                'border-0 focus:ring-2 focus:ring-gray-300'
            ).on_click(increment).mark('increment-button')