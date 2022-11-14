from routes import router


try:
    if __name__ == "__main__":
        router.generate()
except ValueError:
    print("WRONG INPUT")
