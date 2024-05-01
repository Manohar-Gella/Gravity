use actix_web::{web, Scope};

pub fn config(cfg: &mut web::ServiceConfig) {
    cfg.service(web::scope("/api").configure(api_routes));
}

fn api_routes(cfg: &mut web::ServiceConfig) {
    // Define API routes here
}
