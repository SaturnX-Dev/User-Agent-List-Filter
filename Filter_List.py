import os

# Función para filtrar User Agents por navegador
def filter_by_browser(user_agents, browser):
    filtered_agents = [ua for ua in user_agents if browser.lower() in ua.lower()]
    return filtered_agents

# Función para filtrar User Agents por sistema operativo
def filter_by_os(user_agents, os_name):
    if os_name.lower() == 'mac os x':
        filtered_agents = [ua for ua in user_agents if 'mac os x' in ua.lower() and 'iphone' not in ua.lower() and 'ipad' not in ua.lower()]
    elif os_name.lower() == 'ios':
        filtered_agents = [ua for ua in user_agents if 'iphone' in ua.lower() or 'ipad' in ua.lower()]
    elif os_name.lower() == 'linux':
        filtered_agents = [ua for ua in user_agents if 'linux' in ua.lower() and 'android' not in ua.lower()]
    elif os_name.lower() == 'android':
        filtered_agents = [ua for ua in user_agents if 'android' in ua.lower()]
    else:
        filtered_agents = [ua for ua in user_agents if os_name.lower() in ua.lower()]
    
    return filtered_agents

# Función para guardar los resultados en un archivo de texto
def save_results(results):
    file_name = input("Ingresa el nombre del archivo para guardar los resultados (sin extensión): ")
    file_name += ".txt"
    with open(file_name, 'w') as file:
        for result in results:
            file.write(result + '\n')
    print(f"Resultados guardados en '{file_name}'")

# Función principal
def main():
    with open('User Agents List.txt', 'r') as file:
        user_agents = file.read().splitlines()

    while True:
        print("""
 ___________________________________________________________________________________
|                                                                                   |
|                               User Agent List Filter                              |
|                                   by Saturnx-Dev                                  |
|             _________________________________________________________             |
|                                                                                   | 
|                                   |  MAIN MENU |                                  |
|               https://github.com/SaturnX-Dev/User-Agent-List-Filter               |
|                                  Made with love <3                                |
|          _______________________________________________________________          |
|                                                                                   |
|              Filtra una lista de User Agents por SO o por Navegador.              |
|          _______________________________________________________________          |
|                                                                                   |
|      [1] Filtrar por Navegador     | Filtra los User Agents por navegador         |
|      [2] Filtrar por SO            | Filtra los User Agents por sistema operativo |
|      [3] Salir                     | Salir del programa                           |
|                                                                                   |
|___________________________________________________________________________________|

        """)
        option = input("Selecciona una opción (1, 2, 3): ")

        if option == '1':
            print("""
 _______________________________________________________________________________
|                                                                               |
|                                | BROWSER MENU |                               |
|           _________________________________________________________           |
|                                                                               |
|                  User Agent List Filter V1 by Saturnx-Dev                     |
|        _______________________________________________________________        |
|                                                                               |
|            Selecciona un navegador para filtrar los User Agents.              |
|        _______________________________________________________________        |
|                                                                               |
|      [1] Chrome                    | Filtrar User Agents de Chrome            |
|      [2] Safari                    | Filtrar User Agents de Safari            |
|      [3] Firefox                   | Filtrar User Agents de Firefox           |
|      [4] Volver al Menú Principal  | Regresar al Menú Principal               |
|                                                                               |
|_______________________________________________________________________________|
            """)
            browser_option = input("Selecciona una opción (1, 2, 3, 4): ")
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

            # Opción para copiar o guardar los resultados
            save_option = input("\n¿Deseas copiar los resultados (c) o guardarlos en un archivo (g)? (Presiona Enter para continuar): ")
            if save_option.lower() == 'g':
                save_results(filtered_agents)

        elif option == '2':
            print("""
 _______________________________________________________________________________
|                                                                               |
|                            | OPERATING SYSTEM MENU |                          |
|           _________________________________________________________           |
|                                                                               |
|                   User Agent List Filter V1 by Saturnx-Dev                    |
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
            os_option = input("Selecciona una opción (1, 2, 3, 4, 5, 6): ")
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

            # Opción para copiar o guardar los resultados
            save_option = input("\n¿Deseas copiar los resultados (c) o guardarlos en un archivo (g)? (Presiona Enter para continuar): ")
            if save_option.lower() == 'g':
                save_results(filtered_agents)

        elif option == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

        # Después de imprimir los resultados, esperar a que el usuario presione Enter
        input("\nPresiona Enter para volver al menú principal...")

if __name__ == "__main__":
    main()
