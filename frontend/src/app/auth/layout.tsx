import React from "react";

const layout = ({ children }: Readonly<{ children: React.ReactNode }>) => {
  return (
    <div className="flex items-center  justify-center h-[calc(100vh-5rem)] ">
      {children}
    </div>
  );
};

export default layout;
