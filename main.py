from time import sleep
import monitor
import switches


def main():
    monitor.display("", "Job Agnostic", "Button Box", "")
    position = switches.get_left()

    sleep(1)
    module = None

    try:
        if position == 1:
            from _combine import Combine
            module = Combine()
        elif position == 2:
            from _module2 import Module2
            module = Module2()
        elif position == 3:
            from _module3 import Module3
            module = Module3()

        if module:
            module_name = module.__class__.__name__
            monitor.display("Loading", module_name, "", "")
            sleep(1)
            monitor.clear()
            sleep(0.25)

            module.step()
        else:
            raise ImportError("No valid module")

    except KeyboardInterrupt:
        if module:
            module_name = module.__class__.__name__
        else:
            module_name = "Unknown"

        monitor.display("Error:", f"{module_name}", "Interrupted", "")
        print(f"Error in {module_name}: Interrupted")

    except ImportError as e:
        monitor.display("Error:", "Invalid", "module selected", "")
        print(e)


if __name__ == "__main__":
    main()
