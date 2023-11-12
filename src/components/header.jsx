'use client';

import { Disclosure } from "@headlessui/react";
import { PhoneIcon, MapIcon } from "@heroicons/react/24/outline";

import Image from "next/image";
import Logo from "../assets/images/logo.jpg";

function NavbarLogo() {
  return (
    <div className="flex-1 flex items-center">
      <Image className="block h-16 w-auto" src={Logo} alt="Workflow" />
      {/* <h1 className="mr-3 text-xl font-medium text-gray-800">سـفــره</h1> */}
    </div>
  );
}

function NavbarMenuItems() {
  return (
    <div className="flex-1 justify-center flex space-x-8 space-x-reverse">
      <a
        href="#"
        className="w-20 justify-center border-primary text-primary inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
      >
        منو
      </a>
      <a
        href="#"
        className="w-20 justify-center border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
      >
        درباره ما
      </a>
    </div>
  );
}

function NavbarActions() {
  return (
    <div className="flex-1 justify-end ml-6 flex items-center space-x-2 space-x-reverse">
      <button
        type="button"
        className="bg-primary bg-opacity-25 p-2 rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      >
        <PhoneIcon className="h-5 w-5 text-primary" aria-hidden="true" />
      </button>
      <button
        type="button"
        className="bg-primary bg-opacity-25 p-2 rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      >
        <MapIcon className="h-5 w-5 text-primary" aria-hidden="true" />
      </button>
    </div>
  );
}

export default function Header() {
  return (
    <Disclosure as="nav" className="bg-white shadow">
      {({ open }) => (
        <>
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex h-16">
              <NavbarLogo />
              <NavbarMenuItems />
              <NavbarActions />
            </div>
          </div>
        </>
      )}
    </Disclosure>
  );
}
