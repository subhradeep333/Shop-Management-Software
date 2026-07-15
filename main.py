from Modules.auth import login

print("=" * 50)
print("     LOCAL SHOP MANAGEMENT SYSTEM")
print("=" * 50)

if login():
    print("\nWelcome Admin!")
else:
    print("\nAccess Denied.")