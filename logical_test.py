
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def number_to_thai(number):
    digits = [int(digit) for digit in str(number)]
    digits = [0 for _ in range(7-len(digits))] + digits

    # for all digit except สิบ,หน่วย
    thai_digit_dict = {
        1: 'หนึ่ง',
        2: 'สอง',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า',
    }
    thai_digit_tenth_dict = {
        1: '',
        2: 'ยี่',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า',
    }
    thai_digit_oneth_dict = {
        1: 'เอ็ด',
        2: 'สอง',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า',
    }

    if number == 0:
        return 'ศูนย์'
    if number < 10:
        return thai_digit_dict[number]

    thai_text = ''
    if digits[0] != 0:
        thai_text += thai_digit_dict[digits[0]]
        thai_text += 'ล้าน'
    if digits[1] != 0:
        thai_text += thai_digit_dict[digits[1]]
        thai_text += 'แสน'
    if digits[2] != 0:
        thai_text += thai_digit_dict[digits[2]]
        thai_text += 'หมื่น'
    if digits[3] != 0:
        thai_text += thai_digit_dict[digits[3]]
        thai_text += 'พัน'
    if digits[4] != 0:
        thai_text += thai_digit_dict[digits[4]]
        thai_text += 'ร้อย'
    if digits[5] != 0:
        thai_text += thai_digit_tenth_dict[digits[5]]
        thai_text += 'สิบ'
    if digits[6] != 0:
        thai_text += thai_digit_oneth_dict[digits[6]]

    return thai_text
