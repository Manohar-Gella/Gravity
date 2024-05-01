const Builder = @import("std").build.Builder;

pub fn build(b: *Builder) void {
    const exe = b.addExecutable("frontend", "src/main.zig");
    exe.addPackagePath("http_client", "src/http_client.zig");
    exe.addPackagePath("user_interface", "src/user_interface.zig");
    exe.install();
    exe.installBin("frontend");
}
