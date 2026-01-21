# BloodConnect Frontend

A Next.js + React frontend for the BloodConnect blood donation platform.

## Getting Started

### Prerequisites
- Node.js 16+ and npm

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

### Building for Production

```bash
npm run build
npm start
```

## Environment Variables

Create a `.env.local` file:

```
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## Project Structure

- `pages/` - Next.js pages and routing
- `components/` - Reusable React components
- `styles/` - Global CSS and Tailwind configuration
- `utils/` - Utility functions including API client

## Technologies

- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- Axios
