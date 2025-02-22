import React from "react";
import { Link } from "react-router-dom";

function BaseLayout({ children }) {
  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-800 text-white p-5">
        <h1 className="text-xl font-bold mb-6">Admin Dashboard</h1>
        <nav>
          <ul className="space-y-4">
            <li><Link to="#" className="block p-2 hover:bg-gray-700 rounded">Users</Link></li>
            <li><Link to="#" className="block p-2 hover:bg-gray-700 rounded">Cars</Link></li>
            <li><Link to="#" className="block p-2 hover:bg-gray-700 rounded">Services</Link></li>
            <li><Link to="#" className="block p-2 hover:bg-gray-700 rounded">Logout</Link></li>
            <li><Link to="#" className="block p-2 hover:bg-gray-700 rounded">Search</Link></li>
          </ul>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6 bg-gray-100">
        {children}
      </main>
    </div>
  );
}

export default BaseLayout;
