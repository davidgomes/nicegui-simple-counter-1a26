from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value in user storage to persist across sessions
        if 'count' not in app.storage.user:
            app.storage.user['count'] = 0
        
        # Main container with centered layout
        with ui.column().classes('items-center justify-center min-h-screen gap-8 bg-gray-50'):
            # Counter display
            counter_label = ui.label().classes('text-8xl font-light text-gray-800').mark('counter')
            
            # Increment button
            ui.button('+', on_click=lambda: increment()).classes(
                'text-4xl w-20 h-20 rounded-full bg-blue-500 text-white hover:bg-blue-600 shadow-lg'
            ).mark('increment')
        
        def update_display():
            """Update the counter display"""
            counter_label.text = str(app.storage.user['count'])
        
        def increment():
            """Increment the counter"""
            app.storage.user['count'] += 1
            update_display()
        
        # Initialize display
        update_display()