import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    // Needed for large ZIP/JAR imports that pass through middleware/proxy.
    // Next.js defaults this buffered body limit to 10MB.
    proxyClientMaxBodySize: "100mb",
  },
};

export default nextConfig;
