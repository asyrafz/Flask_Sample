import React, { useEffect, useRef } from 'react';

function VideoStream() {
  const imgRef = useRef(null);

  useEffect(() => {
    const img = imgRef.current;
    img.src = 'http://your_server_ip:5000/video_feed';
  }, []);

  return (
    <div>
      <img ref={imgRef} alt="Video stream" />
    </div>
  );
}

export default VideoStream;
