import os

os.system("proot-distro login distro --user user")
user = input(
    "Enter a username to login to the huntrix distro ( as a kpop demon hunter huntrix fans ): \n"
)


class login_huntrix_distro:
    def __init__(self, user):
        self.user = user

    def login(self):
        os.system(f"proot-distro login huntrix_kpdh --user {self.user}")


distro_name = input(
    "Enter the name of the distro you want to login to (e.g., huntrix_kpdh): \n"
)
if distro_name != "huntrix_kpdh":
    os.system("proot-distro rename distro_name")
login_instance = login_huntrix_distro(user)
