from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value in user storage
        if 'count' not in app.storage.user:
            app.storage.user['count'] = 0
        
        def increment():
            """Increment the counter and update display with toast notification"""
            app.storage.user['count'] += 1
            counter_label.text = str(app.storage.user['count'])
            
            # Show toast notification with feedback
            ui.notify(
                f'Counter incremented to {app.storage.user["count"]}',
                type='positive',
                position='top-right',
                timeout=2000,
                close_button=True
            )
        
        # Main container with minimal, clean background
        with ui.column().classes('items-center justify-center min-h-screen gap-20 bg-gray-50'):
            
            # Counter display - significantly larger and red
            counter_label = ui.label(str(app.storage.user['count'])).classes(
                'text-[20rem] font-thin text-red-600 select-none tracking-wider '
                'drop-shadow-lg transition-all duration-300 hover:text-red-700'
            ).mark('counter-display')
            
            # Circular increment button - clean and minimalist
            ui.button('', icon='add').classes(
                'w-16 h-16 rounded-full bg-white hover:bg-gray-100 '
                'text-gray-600 hover:text-gray-700 shadow-md hover:shadow-lg '
                'border-0 transition-all duration-200 ease-out '
                'focus:ring-2 focus:ring-gray-200 focus:ring-opacity-50 focus:outline-none '
                'active:scale-95 hover:scale-105'
            ).on_click(increment).mark('increment-button')