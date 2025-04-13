export function formatDate(datetime) {
      if (!datetime) return '';
            const date = new Date(datetime);

      return date.toLocaleString('en-US', { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric', 
            hour: '2-digit', 
            minute: '2-digit', 
            hour12: true 
      });
}