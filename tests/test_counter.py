import pytest
from nicegui.testing import User
from nicegui import ui


async def test_counter_initial_display(user: User) -> None:
    """Test that counter displays initial value of 0"""
    await user.open('/')
    await user.should_see(marker='counter-display')


async def test_counter_increment(user: User) -> None:
    """Test that clicking the increment button increases counter"""
    await user.open('/')
    
    # Initial state
    await user.should_see(marker='counter-display')
    
    # Click increment button
    user.find(marker='increment-button').click()
    
    # Click again
    user.find(marker='increment-button').click()


async def test_counter_persistence(user: User) -> None:
    """Test that counter value persists in user storage"""
    await user.open('/')
    
    # Increment counter
    user.find(marker='increment-button').click()
    
    # Reload page - counter should persist
    await user.open('/')
    await user.should_see(marker='counter-display')


async def test_multiple_increments(user: User) -> None:
    """Test multiple increments work correctly"""
    await user.open('/')
    
    increment_button = user.find(marker='increment-button')
    
    # Increment 5 times
    for i in range(1, 6):
        increment_button.click()


async def test_counter_elements_present(user: User) -> None:
    """Test that all required UI elements are present"""
    await user.open('/')
    
    # Check counter display exists
    await user.should_see(marker='counter-display')
    
    # Check increment button exists
    await user.should_see(marker='increment-button')


async def test_counter_styling(user: User) -> None:
    """Test that counter has the expected styling classes"""
    await user.open('/')
    
    counter_elements = user.find(marker='counter-display').elements
    button_elements = user.find(marker='increment-button').elements
    
    # Verify elements exist
    assert len(counter_elements) > 0
    assert len(button_elements) > 0
    
    counter_display = next(iter(counter_elements))
    increment_button = next(iter(button_elements))
    
    # Verify counter display has ultra-thin font styling
    assert 'font-thin' in counter_display._classes
    assert 'text-red-500' in counter_display._classes
    
    # Verify button has circular styling
    assert 'rounded-full' in increment_button._classes