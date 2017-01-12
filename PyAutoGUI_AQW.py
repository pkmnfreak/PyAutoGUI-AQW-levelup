import pyautogui
pyautogui.FAILSAFE = True #with the the screen as big as it can be but not full screen
def Attack():
    mana = 100
    pyautogui.moveTo(618, 670) #click Attack
    while mana >= 12:
        pyautogui.click()
        pyautogui.PAUSE = 2
        mana -= 12
    if mana < 12:
        pyautogui.moveTo(186,501) #Move out of the screen
        pyautogui.click()
        pyautogui.PAUSE = 1
        pyautogui.moveTo(815, 684) #click rest
        pyautogui.click()
        pyautogui.PAUSE = 10
        pyautogui.moveTo(1097,487) #Go back to original screen
        pyautogui.click()
        pyautogui.PAUSE = 1
        return Attack()

Attack()
