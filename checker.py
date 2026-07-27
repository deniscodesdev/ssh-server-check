from rich.console import Console
from rich.table import Table
from exporter import export_json

from ssh_client import connect, run_command

console = Console()


async def check_server(host: str, username: str, password: str):
    console.print("[cyan]Connecting...[/cyan]")

    try:
        async with await connect(host, username, password) as conn:

            table = Table(title="SSH Server Information")

            table.add_column("Parameter", style="cyan")
            table.add_column("Value", style="green")

            os_name = await run_command(conn, "cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2")
            uptime = await run_command(conn, "uptime -p")
            cpu = await run_command(conn, "nproc")
            ram = await run_command(conn, "free -h | awk '/Mem:/ {print $2}'")
            disk = await run_command(conn, "df -h / | awk 'NR==2 {print $2}'")
            kernel = await run_command(conn, "uname -r")
            hostname = await run_command(conn, "hostname")
            python_version = await run_command(conn, "python3 --version")
            server_time = await run_command(conn, "date")
            processes = await run_command(conn, "ps -e --no-headers | wc -l")
            load = await run_command(conn, "cat /proc/loadavg | awk '{print $1,$2,$3}'")
            disk_usage = await run_command(conn, "df -h / | awk 'NR==2 {print $5}'")
            ram_usage = await run_command(conn, "free | awk '/Mem:/ {printf(\"%.0f%%\", $3/$2*100)}'")
            public_ip = await run_command(conn, "curl -s https://api.ipify.org")
            architecture = await run_command(conn, "uname -m")
            virtualization = await run_command(conn, "systemd-detect-virt || echo none")
            logged_users = await run_command(conn, "who | wc -l")
            report = {
    "hostname": hostname,
    "public_ip": public_ip,
    "os": os_name.replace('"', ""),
    "kernel": kernel,
    "cpu_cores": cpu,
    "cpu_load": load,
    "ram_total": ram,
    "ram_usage": ram_usage,
    "disk_total": disk,
    "disk_usage": disk_usage,
    "uptime": uptime,
    "python": python_version,
    "architecture": architecture,
    "virtualization": virtualization,
    "logged_users": logged_users,
    "server_time": server_time,
}
            table.add_row("Public IP", public_ip)
            table.add_row("Python", python_version)
            table.add_row("Architecture", architecture)
            table.add_row("Virtualization", virtualization)
            table.add_row("Logged Users", logged_users)
            table.add_row("CPU Load", load)
            table.add_row("RAM Usage", ram_usage)
            table.add_row("Disk Usage", disk_usage)
            table.add_row("Processes", processes)
            table.add_row("Server Time", server_time)  
            table.add_row("Hostname", hostname)
            table.add_row("OS", os_name.replace('"', ""))
            table.add_row("Kernel", kernel)
            table.add_row("CPU Cores", cpu)
            table.add_row("RAM", ram)
            table.add_row("Disk", disk)
            table.add_row("Uptime", uptime)
            export_json(report)
            console.print(table)

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")