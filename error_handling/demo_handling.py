# # while True:
# #     try:
# #         x = int(input())
# #         break
# #     except ValueError:
# #         print('Not a number, try again: ')
# #
# # while True:
# #     try:
# #         x = int(input())
# #         break
# #     # either ValueError or TypeError
# #     except (ValueError, TypeError):
# #         print('Not a number, try again: ')
#
# while True:
# try:
#     x = int(input())
#     break
# # ValueError
# except ValueError as err:
#     print(err)
#     print('ValueError: Not a number, try again: ')
# # TypeError
# except TypeError:
#     print('TypeError: Not a number, try again: ')
# except (IndexError, KeyError) as err:
#     pass
#
#
#
# print(x)
#
#
# try:
#     executeFlow()
# except Exception as err:
#     # log(err)
#     raise err


#
# try:
#     # use file
#     file = open('demo.py', 'r')
#     pass
# finally:
#     file.close()
#
# try:
#     print('In try')
#     int('asd')
# except Exception as ex:
#     print('In except')
#     raise ex
# finally:
#     print('After exception in try')
#
# print('After try-except block')


try:
    raise ValueError()
except ValueError as err:
    print(f'Value error: {err}')
except Exception as err:
    print(f'Base exception: {err}')
except:
    print('Global exception')

