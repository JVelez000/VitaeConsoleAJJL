import json
import re
from fpdf import FPDF

danger = "\033[91m"  
warning = "\033[93m" 
success = "\033[92m" 
reset = "\033[0m"    

def load_data():
    global data
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}


def save_data():
    global data
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def message_danger(text):
  print(f"{danger}{text}{reset}")

def message_warning(text):
  print(f"{warning}{text}{reset}")

def message_success(text):
	print(f"{success}{text}{reset}")

data = {}

def input_texto(label):
    while True:
        valor = input(label)
        if re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', valor) and valor.strip():
            return valor
        else:
            message_danger("❌ Solo letras y espacios. No se permiten caracteres especiales.")

def input_direccion(label):
    while True:
        valor = input(label)
        if re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s#\-]+$', valor) and valor.strip():
            return valor
        else:
            message_danger("❌ Dirección inválida. Solo letras, números, espacios, # y -.")

def input_numero(label):
    while True:
        valor = input(label)
        if valor.isdigit():
            return valor
        else:
            message_danger("❌ Solo se permiten números.")

def input_correo(label):
    while True:
        valor = input(label)
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', valor):
            return valor
        else:
            message_danger("❌ Correo inválido.")

def input_fecha(label):
    while True:
        valor = input(label)
        if re.match(r'^\d{2}/\d{2}/\d{4}$', valor):
            return valor
        else:
            message_danger("❌ Fecha inválida. Formato esperado: dd/mm/yyyy.")

def input_alphanumeric(prompt):
    while True:
        value = input(prompt)
        if re.match(r'^[a-zA-Z0-9\sáéíóúÁÉÍÓÚñÑ]+$', value):
            return value
        else:
            message_danger("❌ Solo se permiten letras, números y espacios (sin caracteres especiales).")

def validate_date(value):
    return value.isnumeric() and int(value) > 0

def validate_str(value):
    return value.strip() != "" and value.isalpha()


def add_user():
    global data

    while True:
        id = input("Ingresa el ID del usuario: ")
        if id.isdigit() and int(id) > 0:
            if id not in data:
                break
            else:
                message_warning("⚠️ Ese ID ya está en uso.")
        else:
            message_danger("❌ Solo se permiten números positivos.")

    name = input_texto("Ingresa el nombre del usuario: ")
    contact = input_numero("Ingresa el contacto del usuario: ")
    address = input_direccion("Ingresa la dirección del usuario: ")
    email = input_correo("Ingresa el correo del usuario: ")
    bdate = input_fecha("Ingresa la fecha de nacimiento del usuario: ")

    data[id] = {
        "id": id,
        "name": name,
        "contact": contact,
        "address": address,
        "email": email,
        "bdate": bdate,
        "references": [],
        "skills_certifications": []
    }

    save_data()
    message_success(f"✔️ Usuario {name} agregado exitosamente.")
    return id

def academic_data(user_id):
    global data

    while True:
        institution = input_texto("Agregue la universidad: ")
        if validate_str(institution):
            break
        else:
            message_danger("❌ Ingresa un valor válido para la institución.")

    while True:
        title = input_texto("Título académico: ")
        if validate_str(title):
            break
        else:
            message_danger("❌ Ingresa un valor válido para el título.")

    while True:
        duration = input_numero("¿En qué año se graduó?: ")
        if validate_date(duration):
            break
        else:
            message_danger("❌ Ingresa un año válido (ej. 2022).")

    data[user_id]["academic"] = {
        "institution": institution,
        "title": title,
        "duration": duration
    }
    save_data()
    message_success("✔️ Datos académicos agregados correctamente.")

def add_experience(user_id):
    global data

    company = input_alphanumeric("Nombre de la empresa: ")
    position = input_texto("Cargo ocupado: ")
    functions = input_texto("Funciones del cargo: ")

    while True:
        duration = input_numero("Duración en la empresa (en años o meses): ")
        if duration.isdigit() and int(duration) > 0:
            break
        else:
            message_danger("❌ Solo se permiten números positivos.")

    data[user_id]["experience"] = {
        "company": company,
        "position": position,
        "functions": functions,
        "duration": duration
    }

    save_data()
    message_success("✔️ Experiencia laboral agregada correctamente.")

def personal_references(user_id):
    global data
    while True:
        ref = {
            "name": input_texto("Nombre de la referencia personal: "),
            "relation": input_texto("Relación con la referencia: "),
            "contact": input_numero("Contacto de la referencia: ")
        }
        data[user_id]["references"].append(ref)
        break

    save_data()
    message_success("✔️ Referencia personal agregada correctamente.")

def skills_certifications(user_id):
    global data

    skill_certification = {
        "skill_or_certification": input_texto("Habilidad o certificación: ")
    }
    data[user_id]["skills_certifications"].append(skill_certification)
    save_data()
    message_success("✔️ Habilidad o certificación agregada correctamente.")

# Funciones nuevas para mostrar listas disponibles

def show_names():
    if not data:
        message_warning("⚠ No hay usuarios registrados.")
        return
    print("Nombres disponibles:")
    for user in data.values():
        print(f"- {user['name']}")

def show_ids():
    if not data:
        message_warning("⚠ No hay usuarios registrados.")
        return
    print("IDs disponibles:")
    for id in data.keys():
        print(f"- {id}")

def show_emails():
    if not data:
        message_warning("⚠ No hay usuarios registrados.")
        return
    print("Correos disponibles:")
    for user in data.values():
        print(f"- {user['email']}")



def search_by_name():
    load_data()
    show_names()  # Muestro los nombres disponibles antes
    name = input("Ingresa el nombre del usuario que deseas buscar: ").strip().lower()
    found = False
    for user in data.values():
        if user["name"].lower() == name:
            print_user_details(user)
            found = True
            break
    if not found:
        message_warning("⚠ No se encontró el usuario con ese nombre.")

def search_by_id():
    load_data()
    show_ids()  # Muestro los IDs disponibles antes
    id = input("Ingresa el ID del usuario que deseas buscar: ").strip()
    if id in data:
        print_user_details(data[id])
    else:
        message_warning("⚠ No se encontró el usuario con ese ID.")

def search_by_email():
    load_data()
    show_emails()  # Muestro los emails disponibles antes
    email = input("Ingresa el correo del usuario que deseas buscar: ").strip().lower()
    found = False
    for user in data.values():
        if user["email"].lower() == email:
            print_user_details(user)
            found = True
            break
    if not found:
        message_warning("⚠ No se encontró el usuario con ese correo.")

def big_filter():
    load_data()
    if not data:
        message_warning("⚠ No hay usuarios registrados para filtrar.")
        return

    while True:
        print("\n--- Filtros disponibles ---")
        print("1. Filtrar por meses/años de experiencia")
        print("2. Filtrar por institución académica")
        print("3. Filtrar por habilidad o certificación")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            experiencia_min = input_numero("¿Cuántos meses/años mínimo de experiencia deseas?: ")
            encontrados = []
            for user in data.values():
                exp = user.get("experience", {})
                if exp and exp.get("duration") and exp["duration"].isdigit():
                    if int(exp["duration"]) >= int(experiencia_min):
                        encontrados.append(user)

            if encontrados:
                print(f"\nUsuarios con al menos {experiencia_min} meses/años de experiencia:")
                for u in encontrados:
                    print_user_details_months(u)
            else:
                message_warning("⚠ No se encontraron usuarios con esa experiencia.")

        elif opcion == "2":
            instituciones = set()
            for user in data.values():
                academic = user.get("academic")
                if academic:
                    instituciones.add(academic.get("institution", "").lower())

            if not instituciones:
                message_warning("⚠ No hay instituciones registradas.")
                continue

            print("\n📚 Instituciones disponibles:")
            for i in instituciones:
                print(f"- {i}")

            seleccion = input("Escribe el nombre de la institución para filtrar: ").strip().lower()
            encontrados = [user for user in data.values() if user.get("academic", {}).get("institution", "").lower() == seleccion]

            if encontrados:
                print(f"\nUsuarios que estudiaron en '{seleccion}':")
                for u in encontrados:
                    print_user_details_academic(u)
            else:
                message_warning("⚠ No se encontraron usuarios en esa institución.")

        elif opcion == "3":
            termino = input_texto("Escribe la habilidad o certificación a buscar: ").strip().lower()
            encontrados = []
            for user in data.values():
                skills = user.get("skills_certifications", [])
                for s in skills:
                    if termino in s.get("skill_or_certification", "").lower():
                        encontrados.append(user)
                        break

            if encontrados:
                print(f"\nUsuarios con habilidad o certificación relacionada con '{termino}':")
                for u in encontrados:
                    print_user_details_skills(u)
            else:
                message_warning("⚠ No se encontraron usuarios con esa habilidad o certificación.")

        elif opcion == "4":
            break
        else:
            message_danger("❌ Opción inválida. Intenta de nuevo.")


def print_user_details_months(user):
    
    print("\n🧑‍💼 Información del usuario:")
    print(f"🆔 ID: {user.get('id', 'N/A')}")
    print(f"👤 Nombre: {user.get('name', 'N/A')}")

    experience = user.get("experience")
    if experience:
        print("\n💼 Experiencia laboral:")
        print(f"  🏢 Empresa: {experience.get('company', 'N/A')}")
        print(f"  📌 Cargo: {experience.get('position', 'N/A')}")
        print(f"  📝 Funciones: {experience.get('functions', 'N/A')}")
        print(f"  ⏳ Duración: {experience.get('duration', 'N/A')}")

def print_user_details_academic(user):
    print("\n🧑‍💼 Información del usuario:")
    print(f"🆔 ID: {user.get('id', 'N/A')}")
    print(f"👤 Nombre: {user.get('name', 'N/A')}")

    academic = user.get("academic")
    if academic:
        print("\n🎓 Formación académica:")
        print(f"  🏫 Institución: {academic.get('institution', 'N/A')}")
        print(f"  🎖️ Título: {academic.get('title', 'N/A')}")
        print(f"  📅 Año de graduación: {academic.get('duration', 'N/A')}")

def print_user_details_skills(user):
    print("\n🧑‍💼 Información del usuario:")
    print(f"🆔 ID: {user.get('id', 'N/A')}")
    print(f"👤 Nombre: {user.get('name', 'N/A')}")

    skills = user.get("skills_certifications", [])
    if skills:
        print("\n🛠️ Habilidades y certificaciones:")
        for s in skills:
            print(f"  - {s.get('skill_or_certification', 'N/A')}")

def print_user_details(user):
    print("\n🧑‍💼 Información del usuario:")
    print(f"🆔 ID: {user.get('id', 'N/A')}")
    print(f"👤 Nombre: {user.get('name', 'N/A')}")
    print(f"📞 Contacto: {user.get('contact', 'N/A')}")
    print(f"🏠 Dirección: {user.get('address', 'N/A')}")
    print(f"📧 Correo: {user.get('email', 'N/A')}")
    print(f"🎂 Fecha de nacimiento: {user.get('bdate', 'N/A')}")

    experience = user.get("experience")
    if experience:
        print("\n💼 Experiencia laboral:")
        print(f"  🏢 Empresa: {experience.get('company', 'N/A')}")
        print(f"  📌 Cargo: {experience.get('position', 'N/A')}")
        print(f"  📝 Funciones: {experience.get('functions', 'N/A')}")
        print(f"  ⏳ Duración: {experience.get('duration', 'N/A')}")

    academic = user.get("academic")
    if academic:
        print("\n🎓 Formación académica:")
        print(f"  🏫 Institución: {academic.get('institution', 'N/A')}")
        print(f"  🎖️ Título: {academic.get('title', 'N/A')}")
        print(f"  📅 Año de graduación: {academic.get('duration', 'N/A')}")

    references = user.get("references", [])
    if references:
        print("\n👥 Referencias personales:")
        for ref in references:
            print(f"  👤 Nombre: {ref.get('name', 'N/A')}, 🤝 Relación: {ref.get('relation', 'N/A')}, 📱 Contacto: {ref.get('contact', 'N/A')}")

    skills = user.get("skills_certifications", [])
    if skills:
        print("\n🛠️ Habilidades y certificaciones:")
        for s in skills:
            print(f"  - {s.get('skill_or_certification', 'N/A')}")

def show_data():
    for id, usuario in data.items():
        print(f"ID: {id} -> Nombre: {usuario['name']}")
        

def update_cv():
    global data

    if not data:
        message_warning("⚠ No hay usuarios registrados.")
        return

    print("\n=== Lista de usuarios registrados ===")
    for user_id, user in data.items():
        print(f"{user_id} ==> {user['name']}")

    while True:
        user_id = input("\nIngresa el ID del usuario que deseas modificar: ")
        if user_id in data:
            break
        else:
            message_danger("❌ ID no encontrado. Intenta de nuevo.")

    while True:
        print(f"\n=== Actualizando el CV de {data[user_id]['name']} ===")
        print("1. Actualizar formación académica")
        print("2. Añadir experiencia laboral")
        print("3. Añadir referencia personal")
        print("4. Añadir habilidad o certificación")
        print("5. Volver al menú principal")

        option = input("Selecciona una opción (1-5): ")

        if option == "1":
            academic_data(user_id)
        elif option == "2":
            add_experience(user_id)
        elif option == "3":
            personal_references(user_id)
        elif option == "4":
            skills_certifications(user_id)
        elif option == "5":
            message_success("✔ Regresando al menú principal.")
            break
        else:
            message_warning("⚠ Opción no válida. Intenta de nuevo.")
            

def generate_pdf(user_id):
    global data
    if user_id not in data:
        message_danger("❌ Usuario no encontrado para generar PDF.")
        return
    
    user = data[user_id]
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    
    pdf.cell(0, 10, f"CV de {user.get('name', 'N/A')}", 0, 1, 'C')
    pdf.ln(10)

    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"ID: {user.get('id', 'N/A')}", 0, 1)
    pdf.cell(0, 10, f"Contacto: {user.get('contact', 'N/A')}", 0, 1)
    pdf.cell(0, 10, f"Dirección: {user.get('address', 'N/A')}", 0, 1)
    pdf.cell(0, 10, f"Correo: {user.get('email', 'N/A')}", 0, 1)
    pdf.cell(0, 10, f"Fecha de nacimiento: {user.get('bdate', 'N/A')}", 0, 1)
    pdf.ln(5)

    experience = user.get("experience")
    if experience:
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Experiencia Laboral:", 0, 1)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Empresa: {experience.get('company', 'N/A')}", 0, 1)
        pdf.cell(0, 10, f"Cargo: {experience.get('position', 'N/A')}", 0, 1)
        pdf.cell(0, 10, f"Funciones: {experience.get('functions', 'N/A')}", 0, 1)
        pdf.cell(0, 10, f"Duración: {experience.get('duration', 'N/A')}", 0, 1)
        pdf.ln(5)

    academic = user.get("academic")
    if academic:
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Formación Académica:", 0, 1)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Institución: {academic.get('institution', 'N/A')}", 0, 1)
        pdf.cell(0, 10, f"Título: {academic.get('title', 'N/A')}", 0, 1)
        pdf.cell(0, 10, f"Año de graduación: {academic.get('duration', 'N/A')}", 0, 1)
        pdf.ln(5)

    references = user.get("references", [])
    if references:
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Referencias Personales:", 0, 1)
        pdf.set_font("Arial", '', 12)
        for ref in references:
            pdf.cell(0, 10, f"Nombre: {ref.get('name', 'N/A')}, Relación: {ref.get('relation', 'N/A')}, Contacto: {ref.get('contact', 'N/A')}", 0, 1)
        pdf.ln(5)

    skills = user.get("skills_certifications", [])
    if skills:
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Habilidades y Certificaciones:", 0, 1)
        pdf.set_font("Arial", '', 12)
        for s in skills:
            pdf.cell(0, 10, f"- {s.get('skill_or_certification', 'N/A')}", 0, 1)
        pdf.ln(5)

    filename = f"CV_{user.get('name', 'usuario')}.pdf"
    pdf.output(filename)
    message_success(f"✔️ PDF generado exitosamente: {filename}")
    
def show_data():
    global data
    if not data:
        message_warning("⚠ No hay usuarios registrados para mostrar.")
        return