from nicegui.testing import User
from nicegui import ui, app

async def test_counter_initialization(user: User) -> None:
    """Test that counter initializes with zero"""
    await user.open('/')
    
    # Check that counter displays 0 initially
    await user.should_see('0')
    
    # Verify storage is initialized
    assert app.storage.user['count'] == 0

async def test_counter_increment(user: User) -> None:
    """Test that counter increments when button is clicked"""
    await user.open('/')
    
    # Click increment button
    user.find(marker='increment-button').click()
    
    # Check that counter shows 1
    await user.should_see('1')
    assert app.storage.user['count'] == 1

async def test_multiple_increments(user: User) -> None:
    """Test multiple increments work correctly"""
    await user.open('/')
    
    # Click increment button 3 times
    increment_button = user.find(marker='increment-button')
    for i in range(3):
        increment_button.click()
    
    # Check final count
    await user.should_see('3')
    assert app.storage.user['count'] == 3

async def test_counter_persistence(user: User) -> None:
    """Test that counter value persists in user storage"""
    await user.open('/')
    
    # Increment counter
    user.find(marker='increment-button').click()
    user.find(marker='increment-button').click()
    
    # Verify counter shows 2
    await user.should_see('2')
    
    # Check that value is stored in user storage
    assert app.storage.user['count'] == 2

async def test_ui_elements_present(user: User) -> None:
    """Test that required UI elements are present and properly marked"""
    await user.open('/')
    
    # Check counter display exists
    await user.should_see(marker='counter-display')
    
    # Check increment button exists
    await user.should_see(marker='increment-button')
    
    # Verify button has add icon by checking its properties
    button_elements = user.find(marker='increment-button').elements
    assert len(button_elements) > 0
    button = list(button_elements)[0]
    assert button.props.get('icon') == 'add'