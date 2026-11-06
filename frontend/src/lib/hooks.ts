import { useState, useEffect, useCallback } from 'react';

/**
 * Delays updating a value until the specified delay has elapsed since the last change.
 * Ideal for search inputs to avoid firing requests on every keystroke.
 */
export function useDebounce<T>(value: T, delay: number): T {
    const [debouncedValue, setDebouncedValue] = useState<T>(value);

    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouncedValue(value);
        }, delay);

        return () => clearTimeout(handler);
    }, [value, delay]);

    return debouncedValue;
}

/**
 * Wraps a boolean toggle into a stable callback — avoids
 * re-creating the toggle function on every render.
 */
export function useToggle(initialValue = false): [boolean, () => void, (v: boolean) => void] {
    const [value, setValue] = useState(initialValue);

    const toggle = useCallback(() => setValue(v => !v), []);

    return [value, toggle, setValue];
}
