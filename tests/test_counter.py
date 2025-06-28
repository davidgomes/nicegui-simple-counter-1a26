from nicegui.testing import User
from nicegui import ui, app

async def test_counter_page_loads(user: User) -> None:
    """Test that counter page loads successfully"""
    await user.open('/')
    
    # Check all required elements exist
    await user.should_see(marker='title')
    await user.should_see(marker='counter_display') 
    await user.should_see(marker='increment_btn')
    await user.should_see(marker='reset_btn')

async def test_storage_initialization(user: User) -> None:
    """Test that storage is properly initialized"""
    await user.open('/')
    
    # Check that storage is initialized with correct value
    assert 'counter_value' in app.storage.user
    assert app.storage.user['counter_value'] == 0

async def test_ui_elements_exist(user: User) -> None:
    """Test that UI elements are properly created"""
    await user.open('/')
    
    # Check that we have the expected number of each element type
    assert len(user.find(ui.label).elements) == 2  # title + counter display
    assert len(user.find(ui.button).elements) == 2  # increment + reset
    
    # Check specific markers exist
    assert len(user.find(marker='title').elements) == 1
    assert len(user.find(marker='counter_display').elements) == 1
    assert len(user.find(marker='increment_btn').elements) == 1
    assert len(user.find(marker='reset_btn').elements) == 1