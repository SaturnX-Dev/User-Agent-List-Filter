# Función para filtrar User Agents por navegador
def filter_by_browser(user_agents, browser):
    filtered_agents = [ua for ua in user_agents if browser.lower() in ua.lower()]
    return filtered_agents

# Función para filtrar User Agents por sistema operativo
def filter_by_os(user_agents, os_name):
    if os_name.lower() == 'mac os x':
        # Filtrar solo las entradas específicas de Mac OS X
        filtered_agents = [ua for ua in user_agents if 'mac os x' in ua.lower() and 'iphone' not in ua.lower() and 'ipad' not in ua.lower()]
    else:
        # Filtrar el resto de las entradas por el nombre del sistema operativo
        filtered_agents = [ua for ua in user_agents if os_name.lower() in ua.lower()]
    
    return filtered_agents


# Función principal
def main():
    # Leer el archivo de User Agents
    with open('User Agents List.txt', 'r') as file:
        user_agents = file.read().splitlines()

    while True:
        print("""
 _______________________________________________________________________________
|                                                                               |
|                            User Agent Filter List                             |
|                                by Saturnx-Dev                                 |
|           _________________________________________________________           |
|                                                                               | 
|                                |  MAIN MENU |                                 |
|           _________________________________________________________           |
|                                                                               |
|        _______________________________________________________________        |
|                                                                               |
|        Filtra una lista de User Agents por Equipo, SO o por Navegador.        |
|        _______________________________________________________________        |
|                                                                               |
|      [1] Filtrar por Navegador      | Filtra los User Agents por navegador    |
|      [2] Filtrar por SO        | Filtra los User Agents por sistema operativo |
|      [3] Salir                      | Salir del programa                      |
|                                                                               |
|_______________________________________________________________________________|
    """)
        option = input("Selecciona una opción (1, 2, 3): ")

        if option == '1':
            browser_option = input("""
 _______________________________________________________________________________
|                                                                               |
|                                 | BROWSER MENU |                              |
|           _________________________________________________________           |
|                                                                               |
|        _______________________________________________________________        |
|                                                                               |
|        Selecciona un navegador para filtrar los User Agents.                  |
|        _______________________________________________________________        |
|                                                                               |
|      [1] Chrome                    | Filtrar User Agents de Chrome            |
|      [2] Safari                    | Filtrar User Agents de Safari            |
|      [3] Firefox                   | Filtrar User Agents de Firefox           |
|      [4] Volver al Menú Principal  | Regresar al Menú Principal               |
|                                                                               |
|_______________________________________________________________________________|
            """)
            if browser_option == '1':
                filtered_agents = filter_by_browser(user_agents, 'Chrome')
            elif browser_option == '2':
                filtered_agents = filter_by_browser(user_agents, 'Safari')
            elif browser_option == '3':
                filtered_agents = filter_by_browser(user_agents, 'Firefox')
            elif browser_option == '4':
                continue
            else:
                print("Opción no válida. Inténtalo de nuevo.")

            print("\nUser Agents Filtrados por Navegador:")
            for agent in filtered_agents:
                print(agent)

        elif option == '2':
            os_option = input("""
 _______________________________________________________________________________
|                                                                               |
|                             | OPERATING SYSTEM MENU |                         |
|           _________________________________________________________           |
|                                                                               |
|        _______________________________________________________________        |
|                                                                               |
|        Selecciona un sistema operativo para filtrar los User Agents.          |
|        _______________________________________________________________        |
|                                                                               |
|      [1] Windows                   | Filtrar User Agents de Windows           |
|      [2] Mac OS X                  | Filtrar User Agents de Mac OS X          |
|      [3] Linux                     | Filtrar User Agents de Linux             |
|      [4] Android                   | Filtrar User Agents de Android           |
|      [5] iOS                       | Filtrar User Agents de iOS               |
|      [6] Volver al Menú Principal  | Regresar al Menú Principal               |
|                                                                               |
|_______________________________________________________________________________|
            """)
            if os_option == '1':
                filtered_agents = filter_by_os(user_agents, 'Windows')
            elif os_option == '2':
                filtered_agents = filter_by_os(user_agents, 'Mac OS X')
            elif os_option == '3':
                filtered_agents = filter_by_os(user_agents, 'Linux')
            elif os_option == '4':
                filtered_agents = filter_by_os(user_agents, 'Android')
            elif os_option == '5':
                filtered_agents = filter_by_os(user_agents, 'iOS')
            elif os_option == '6':
                continue
            else:
                print("Opción no válida. Inténtalo de nuevo.")

            print("\nUser Agents Filtrados por Sistema Operativo:")
            for agent in filtered_agents:
                print(agent)

        elif option == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

        # Después de imprimir los resultados, esperar a que el usuario presione Enter
        input("\nPresiona Enter para volver al menú principal...")

if __name__ == "__main__":
    main()
