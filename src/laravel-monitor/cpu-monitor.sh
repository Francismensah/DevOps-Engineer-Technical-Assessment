#!/bin/bash

# Configuration
THRESHOLD=80
SERVICE_NAME="laravel.service"
LOG_FILE="/var/log/laravel-monitor.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

get_cpu_usage() {
    # Get CPU usage of Laravel processes
    cpu_usage=$(ps aux | grep artisan | grep -v grep | awk '{print $3}' | awk '{s+=$1} END {print s}')
    echo "${cpu_usage%.*}"
}

restart_service() {
    log_message "CPU usage exceeded ${THRESHOLD}%. Restarting ${SERVICE_NAME}..."
    systemctl restart "$SERVICE_NAME"
    
    if [ $? -eq 0 ]; then
        log_message "Service restart successful"
    else
        log_message "Service restart failed"
        # Send alert (implement your preferred notification method)
        send_alert "Failed to restart ${SERVICE_NAME}"
    fi
}

send_alert() {
    # Implement your alert mechanism (email, Slack, etc.)
    echo "$1" | mail -s "Laravel Service Alert" admin@example.com
}

# Main monitoring loop
while true; do
    cpu_usage=$(get_cpu_usage)
    
    if [ "$cpu_usage" -gt "$THRESHOLD" ]; then
        restart_service
    fi
    
    # Check every minute
    sleep 60
done