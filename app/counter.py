from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value in user storage to persist across sessions
        if 'count' not in app.storage.user:
            app.storage.user['count'] = 0
        
        # Main container with centered layout
        with ui.column().classes('items-center justify-center min-h-screen gap-8 bg-gray-50'):
            # Counter display with smooth transition
            counter_label = ui.label().classes(
                'text-8xl font-light text-gray-800 transition-all duration-200 ease-in-out'
            ).mark('counter')
            
            # Increment button with active state animation
            ui.button('+', on_click=lambda: increment()).classes(
                'text-4xl w-20 h-20 rounded-full bg-blue-500 text-white hover:bg-blue-600 '
                'active:scale-95 shadow-lg transition-all duration-150 ease-in-out'
            ).mark('increment')
        
        def update_display():
            """Update the counter display with subtle animation"""
            counter_label.text = str(app.storage.user['count'])
            # Add a brief scale animation for visual feedback
            counter_label.classes(remove='scale-110')
            counter_label.classes(add='scale-110')
            ui.timer(0.1, lambda: counter_label.classes(remove='scale-110'))
        
        def increment():
            """Increment the counter"""
            app.storage.user['count'] += 1
            update_display()
        
        # Initialize display
        update_display()