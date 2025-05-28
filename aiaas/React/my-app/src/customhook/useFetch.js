import { useState, useEffect, useRef } from 'react';

/**
 * @param {string} url - 요청할 URL
 * @param {object} options - fetch 옵션 (headers, method 등)
 * @param {boolean} enabled - fetch 실행 여부 (기본값: true)
 * @returns {object} data, error, loading 상태
 */
export function useFetch(url, options = {}, enabled = true) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const optionsRef = useRef(options);

  useEffect(() => {
    if (!enabled || !url) return;

    const controller = new AbortController(); // 요청 중단용
    const signal = controller.signal;

    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await fetch(url, {
          ...optionsRef.current,
          signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        setData(result);
        setError(null);
      } catch (e) {
        if (e.name === 'AbortError') {
          // 요청이 중단된 경우는 무시
          return;
        }
        setError(e);
        setData(null);
      } finally {
        setLoading(false);
      }
    };

    fetchData();

    return () => {
      controller.abort(); // 컴포넌트 언마운트 시 요청 취소
    };
  }, [url, enabled]); // options는 의존성에서 제거

  return { data, error, loading };
}
