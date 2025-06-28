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
    user.find(marker='increment').click()
    
    # Check that counter shows 1
    await user.should_see('1')
    assert app.storage.user['count'] == 1

async def test_multiple_increments(user: User) -> None:
    """Test multiple increments work correctly"""
    await user.open('/')
    
    # Click increment button multiple times
    for i in range(5):
        user.find(marker='increment').click()
    
    # Check final count
    await user.should_see('5')
    assert app.storage.user['count'] == 5

async def test_ui_elements_present(user: User) -> None:
    """Test that required UI elements are present"""
    await user.open('/')
    
    # Check counter display exists
    await user.should_see(marker='counter')
    
    # Check increment button exists
    await user.should_see(marker='increment')
    
    # Verify button shows the plus sign
    await user.should_see('+')