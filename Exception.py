while True :
    try:
        number = int(input("press your number\n"))
        print(24/number)
        break

    except ValueError:
        print("dont pick character")
    except ZeroDivisionError:
        print("Dont press zero")
    except:
        break
    finally:
        print("loop complete")