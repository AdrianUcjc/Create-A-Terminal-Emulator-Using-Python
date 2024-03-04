"""sh
#!/bin/bash

# launcher.sh

echo "Launcher PID: $$"

# Lanzar el programa en Python (programm.py)
python3 programm.py &

# Esperar a que el programa en Python termine
wait $!

# Al finalizar la presentación, obtener el PID del proceso padre (launcher.sh)
parent_pid=$$

# Obtener el PID del hijo usando pstree y awk
child_pid=$(pstree -p $parent_pid | grep -oP '(?<=\()(\d+)(?=\)-programm.py)')

# Si pstree no muestra los PIDs, puedes intentar con 'pgrep'
if [ -z "$child_pid" ]; then
    child_pid=$(pgrep -P $parent_pid -f 'programm.py')
fi

# Mostrar el PID del hijo
echo "Child PID: $child_pid"

# Matar el proceso hijo usando kill -9
kill -9 $child_pid

# Si es necesario, también matar el proceso padre
# kill -9 $parent_pid
"""
