from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value in user storage
        if 'count' not in app.storage.user:
            app.storage.user['count'] = 0
        
        def increment():
            """Increment the counter with toast notification"""
            app.storage.user['count'] += 1
            counter_label.text = str(app.storage.user['count'])
            
            # Subtle toast notification
            ui.notify(
                f'Count: {app.storage.user["count"]}',
                type='info',
                position='top-right',
                timeout=1200,
                close_button=False,
                color='grey-1',
                classes='text-grey-7 font-light text-sm bg-white/90 border border-grey-3 shadow-sm'
            )
        
        # Modern minimalist layout
        with ui.column().classes('items-center justify-center min-h-screen gap-16 bg-grey-1'):
            
            # Exceptionally large counter display with ultra-thin font
            counter_label = ui.label(str(app.storage.user['count'])).classes(
                'text-[20rem] font-thin text-red-500 select-none tracking-wider '
                'transition-all duration-300 ease-out'
            ).style('font-weight: 100; line-height: 0.8;').mark('counter-display')
            
            # Visible and easily clickable circular increment button with add icon
            with ui.button(icon='add').classes(
                'w-24 h-24 rounded-full bg-red-500 hover:bg-red-600 active:bg-red-700 '
                'text-white shadow-lg hover:shadow-xl active:shadow-md '
                'transition-all duration-200 ease-out '
                'focus:outline-none focus:ring-4 focus:ring-red-200 '
                'active:scale-95 hover:scale-105 '
                'border-0'
            ).style(
                'font-size: 2rem;'
            ).on_click(increment).mark('increment-button'):
                pass
            
            # Subtle instruction text
            ui.label('Tap to increment').classes(
                'text-grey-5 font-light text-sm mt-4 opacity-70'
            )
            
        # Add custom styles for modern design
        ui.add_head_html('''
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');
                
                body {
                    font-family: 'Inter', sans-serif;
                    background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
                }
                
                .q-notification {
                    border-radius: 8px !important;
                    backdrop-filter: blur(4px) !important;
                }
                
                .q-btn .q-icon {
                    font-size: inherit !important;
                }
                
                /* Ensure button icon is clearly visible */
                .q-btn[data-cy="increment-button"] .q-icon {
                    color: white !important;
                    font-weight: bold !important;
                }
            </style>
        ''')