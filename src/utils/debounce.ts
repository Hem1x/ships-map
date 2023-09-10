import { useState, useEffect } from 'react';

export const useDebounce = (value: number, delay: number = 300) => {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebounced(value);
    }, delay);

    return () => clearTimeout(handler);
  });

  return debounced;
};
