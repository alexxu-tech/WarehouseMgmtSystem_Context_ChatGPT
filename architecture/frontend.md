# Frontend Architecture

## Purpose
This document describes the frontend architecture of the Warehouse Management System (WMS). It defines the structure, responsibilities, development workflow, and integration strategy of the frontend application.

------------------------------------------------------------------------

## Responsibilities
The frontend is responsible for:
- Rendering user interfaces
- Handling user interactions
- Communicating with backend APIs
- Managing application state
- Displaying validation and system errors
- Providing responsive user experience

------------------------------------------------------------------------

## Technology Stack
- Language: JavaScript / TypeScript
- Build Tool: Vite
- Package Manager: pnpm
- Framework: SPA (React/Vue-ready)
- UI Framework: Ant Design
- Routing: React Router
- HTTP Client: fetch / axios
- Styling: Ant Design / CSS / Utility Framework (planned)

------------------------------------------------------------------------

## Repository Location
Frontend source code is located at:
src/dev/frontend/

------------------------------------------------------------------------

## Project Structure
Typical layout:
src/dev/frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   ├── styles/
│   └── main.ts / main.js
├── public/
├── package.json
├── pnpm-lock.yaml
└── vite.config.js

Notes:
- pnpm-lock.yaml must be committed
- node_modules is ignored
- Build artifacts are not committed

------------------------------------------------------------------------

## Development Server
Start command:
pnpm dev

Default behavior:
- Port: 5173
- Hot Module Reload enabled
- Local development optimized

------------------------------------------------------------------------

## Backend Integration

### API Base URL
Default: http://localhost:8000
Configurable via environment variables.

### Communication Pattern
- All requests use HTTP/REST
- JSON request/response format
- Centralized API service layer

Example:
GET /health
POST /orders
GET /inventory

------------------------------------------------------------------------

## State Management
Current phase:
- Local component state
- Simple service-based state

Future options (if complexity grows):
- Redux
- Zustand
- Pinia

Avoid premature abstraction.

------------------------------------------------------------------------

## UI Architecture
Design principles:
- Component-based structure
- Reusable UI elements
- Clear separation of view and logic
- Consistent layout system

Hierarchy:
Page → Layout → Component → Control

------------------------------------------------------------------------

## Error Handling
Frontend must handle:
- Network failures
- Validation errors
- Authorization errors
- Backend exceptions

Guidelines:
- Display meaningful messages
- Avoid silent failures
- Provide retry options when appropriate

------------------------------------------------------------------------

## Build and Deployment

### Development
pnpm dev

### Production Build
pnpm build

Output: dist/
Static files ready for CDN or backend hosting.

------------------------------------------------------------------------

## Performance Considerations
Planned optimizations:
- Code splitting
- Lazy loading
- Asset compression
- Browser caching
- Bundle analysis

Performance tuning follows functional stability.

------------------------------------------------------------------------

## Accessibility and UX (Planned)
Future improvements:
- Keyboard navigation
- Screen reader support
- Mobile optimization
- Theme support (dark/light)

------------------------------------------------------------------------

## Security (Frontend Scope)
Responsibilities:
- Secure token storage (future)
- XSS prevention
- CSRF-safe patterns
- Avoid sensitive data exposure

Backend remains primary security boundary.

------------------------------------------------------------------------

## Extension Strategy
New frontend features should follow:
1. Create components
2. Add service APIs
3. Integrate state
4. Add tests
5. Update styles

Avoid tightly coupling UI and data logic.

------------------------------------------------------------------------

## Related Documents
- architecture/overview.md
- architecture/backend.md
- decisions/0001-dev-workflow.md
