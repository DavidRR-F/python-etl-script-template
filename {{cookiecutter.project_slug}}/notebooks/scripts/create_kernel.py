import subprocess

def main():
    subprocess.run(["python", "-m", "ipykernel", "install", "--user", "--name=test"], check=True)
    print("Kernel 'mc_enroll' created successfully.")

if __name__ == "__main__":
    main()
