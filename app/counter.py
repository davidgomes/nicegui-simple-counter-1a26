from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value in user storage
        if 'count' not in app.storage.user:
            app.storage.user['count'] = 0
        
        def increment():
            """Increment the counter with seamless visual feedback"""
            app.storage.user['count'] += 1
            counter_label.text = str(app.storage.user['count'])
            
            # Ultra-minimal toast notification
            ui.notify(
                f'{app.storage.user["count"]}',
                type='info',
                position='top',
                timeout=800,
                close_button=False,
                color='transparent',
                classes='text-red-400 font-thin text-lg backdrop-blur-sm bg-white/20 border-0 shadow-none'
            )
        
        # Minimal full-screen layout
        with ui.column().classes('items-center justify-center min-h-screen gap-32 bg-white'):
            
            # Exceptionally large counter display with ultra-thin font
            counter_label = ui.label(str(app.storage.user['count'])).classes(
                'text-[24rem] font-thin text-red-500 select-none tracking-wide '
                'transition-all duration-500 ease-out opacity-90 hover:opacity-100'
            ).style('font-weight: 100; letter-spacing: 0.1em;').mark('counter-display')
            
            # Single elegant circular button - highly subtle
            ui.button('').classes(
                'w-20 h-20 rounded-full bg-transparent hover:bg-red-50/30 '
                'border border-red-200/40 hover:border-red-300/60 '
                'transition-all duration-300 ease-out '
                'focus:outline-none focus:ring-1 focus:ring-red-200/50 '
                'active:scale-95 hover:scale-102 '
                'shadow-sm hover:shadow-md'
            ).style(
                'backdrop-filter: blur(2px);'
            ).on_click(increment).mark('increment-button')
            
        # Add custom styles for ultra-minimal aesthetic
        ui.add_head_html('''
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300&display=swap');
                
                body {
                    font-family: 'Inter', sans-serif;
                    overflow: hidden;
                }
                
                .q-notification {
                    border-radius: 12px !important;
                    backdrop-filter: blur(8px) !important;
                }
                
                .q-btn:before {
                    opacity: 0 !important;
                }
            </style>
        ''')