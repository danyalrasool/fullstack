import os

def main():
    mode = os.getenv("APP_MODE", "development")
    print(f"Hello, World! 👋 api is running in {mode} mode.")

if __name__ == "__main__":
    main()
