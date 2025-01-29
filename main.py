import tkinter as tk
import nmap
import signal

def scan_ports():
    """
    Performs a port scan using nmap and displays the results.
    Handles KeyboardInterrupt gracefully.
    """
    target = target_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    try:
        scanner = nmap.PortScanner()
        # scanner.scan(target, str(start_port) + "-" + str(end_port)) 
        scanner.scan(target, str(start_port) + "-" + str(end_port), arguments='-Pn')  # Add '-Pn' for faster scan (optional)

        results_text.delete(1.0, tk.END)  # Clear previous results

        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                for port in scanner[host][proto].keys():
                    results_text.insert(tk.END, f"Host: {host}\n")
                    results_text.insert(tk.END, f"Protocol: {proto}\n")
                    results_text.insert(tk.END, f"Port: {port}\n")
                    results_text.insert(tk.END, f"State: {scanner[host][proto][port]['state']}\n")
                    results_text.insert(tk.END, f"Service: {scanner[host][proto][port]['name']}\n\n")

    except KeyboardInterrupt:
        print("Scan interrupted by user.")
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Scan interrupted.\n")
    except Exception as e:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"Error: {str(e)}\n")

# Create the main window
root = tk.Tk()
root.title("Simple Port Scanner")

# Create GUI elements
target_label = tk.Label(root, text="Target IP/Hostname:")
target_label.pack()
target_entry = tk.Entry(root, width=30)
target_entry.pack()

start_port_label = tk.Label(root, text="Start Port:")
start_port_label.pack()
start_port_entry = tk.Entry(root, width=10)
start_port_entry.pack()

end_port_label = tk.Label(root, text="End Port:")
end_port_label.pack()
end_port_entry = tk.Entry(root, width=10)
end_port_entry.pack()

scan_button = tk.Button(root, text="Scan", command=scan_ports)
scan_button.pack()

results_text = tk.Text(root, height=20, width=60)
results_text.pack()

root.mainloop()