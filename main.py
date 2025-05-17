from hojasdevida import*

def main_menu():
    load_data()

    while True:
        print("\n---Vitae Console---")
        print("1. Agregar usuario")
        print("2. Consultar cv")
        print("3. Actualizar datos")
        print("4. Exportar cv")
        print("5. Salir")

        choice = input("Selecciona una opción (1-5): ")
        if choice == "1":
            user_id = add_user()
            academic_data(user_id)
            add_experience(user_id)
            personal_references(user_id)
            skills_certifications(user_id)
            save_data()
            show_data()

        elif choice == "2":
            update_cv()

        elif choice == "3":
            update_cv()
        
        elif choice == "4":
            user_id = input("Ingresa el ID del usuario para generar el PDF: ")
            generate_pdf(user_id)

        elif choice == "5":
            print("Saliendo del programa...")
            exit()
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()